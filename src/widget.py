from src.masks import  get_mask_card_number, get_mask_account_long
from datetime import datetime
from typing import Any


def mask_account_card(card_number: str) -> str:
    """Функция которая маскирует номер карты и счёта."""
    if "Счет" in card_number:
        mask_account = f"Счет {get_mask_account_long(card_number[:])}"
        return mask_account
    elif "Счет" not in card_number:
        card_mask = get_mask_card_number(card_number[-16:])
        mask = card_number.replace(card_number[-16:], card_mask)
        return mask


def get_date(data: Any) -> Any:
    """Функция которая возвращает дату."""
    if data == "":
        return ""
    elif data:
        d = datetime.strptime(data, format("%Y-%m-%dT%H:%M:%S.%f"))
        return d.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(get_date("2024-03-11T02:26:18.671407"))
