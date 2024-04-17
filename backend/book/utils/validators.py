from django.core.exceptions import ValidationError


def validate_max_price(value):
    if value > 99999:
        raise ValidationError('Значение не должно превышать 99999')
