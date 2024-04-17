<template>
  <div>
    <h1>Books</h1>

    <table>
      <thead>
      <tr>
        <th v-for="column in visibleColumns" :key="column.id">
          {{ column.column_name }}
        </th>
        <th></th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="book in books" :key="book.id">
        <td v-for="column in visibleColumns" :key="column.id">
          {{ book[column.column_name] }}
        </td>
        <td>
          <button @click="editBook(book)">Edit</button>
          <button @click="deleteBook(book.id)">Delete</button>
        </td>
      </tr>
      </tbody>
    </table>

    <h2>Add new book</h2>
    <form @submit.prevent="addBook">
      <div v-for="column in columns" :key="column.id">
        <label :for="column.column_name">{{ column.column_name }}</label>
        <input :id="column.column_name" v-model="newBook[column.column_name]"/>
        <div v-if="newBookErrors && newBookErrors[column.column_name]">
          <p v-for="error in newBookErrors[column.column_name]" :key="error">{{ error }}</p>
        </div>
      </div>
      <button type="submit">Add</button>
    </form>

    <form v-if="editedBook" @submit.prevent="saveEditedBook">
      <div v-for="column in columns" :key="column.id">
        <label :for="column.column_name">{{ column.column_name }}</label>
        <input :id="column.column_name" v-model="editedBook[column.column_name]"/>
        <div v-if="editedBookErrors && editedBookErrors[column.column_name]">
          <p v-for="error in editedBookErrors[column.column_name]" :key="error">{{ error }}</p>
        </div>
      </div>
      <button type="submit">Save</button>
      <button @click="editedBook = null">Cancel</button>
    </form>

    <h2>Visible Columns</h2>
    <table>
      <thead>
      <tr>
        <th>ID</th>
        <th>Column Name</th>
        <th>Visible</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="column in columns" :key="column.id">
        <td>{{ column.id }}</td>
        <td>{{ column.column_name }}</td>
        <td>
          <input type="checkbox" v-model="column.is_visible"
                 @change="updateColumnVisibility(column.id, column.is_visible)"/>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      columns: [],
      books: [],
      newBook: {},
      newBookErrors: null,
      editedBook: null,
      editedBookErrors: null,
    };
  },
  computed: {
    visibleColumns() {
      return this.columns.filter((column) => column.is_visible);
    },
  },
  async created() {
    const columnsResponse = await axios.get('http://127.0.0.1:8000/api/v1/profile/');
    this.columns = columnsResponse.data;

    const booksResponse = await axios.get('http://127.0.0.1:8000/api/v1/book/');
    this.books = booksResponse.data;
  },
  methods: {
    async updateColumnVisibility(id, is_visible) {
      try {
        await axios.patch(`http://127.0.0.1:8000/api/v1/profile/${id}/`, {is_visible});
      } catch (error) {
        console.error(error);
      }
    },
    async addBook() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/v1/book/', this.newBook);
        this.books.push(response.data);
        this.newBook = {};
      } catch (error) {
        if (error.response && error.response.status === 400) {
          this.newBookErrors = error.response.data;
        } else {
          console.error(error);
        }
      }
    },
    async deleteBook(id) {
      await axios.delete(`http://127.0.0.1:8000/api/v1/book/${id}/`);
      this.books = this.books.filter((book) => book.id !== id);
    },
    editBook(book) {
      this.editedBook = {...book};
    },
    async saveEditedBook() {
      try {
        await axios.put(`http://127.0.0.1:8000/api/v1/book/${this.editedBook.id}/`, this.editedBook);
        const index = this.books.findIndex((book) => book.id === this.editedBook.id);
        this.books.splice(index, 1, this.editedBook);
        this.editedBook = null;
      } catch (error) {
        if (error.response && error.response.status === 400) {
          this.editedBookErrors = error.response.data;
        } else {
          console.error(error);
        }
      }
    },
  },
};
</script>
