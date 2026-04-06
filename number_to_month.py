# Replace the "ANSWER HERE" for your answer

def number_to_month(month):
    if month == 1:
        month_name = "enero"
    elif month == 2:
        month_name = "febrero"
    elif month == 3:
        month_name = "marzo"
    elif month == 4:
        month_name = "abril"
    elif month == 5:
        month_name = "mayo"
    elif month == 6:
        month_name = "junio"
    elif month == 7: 
        month_name = "julio"
    elif month == 8: 
        month_name = "agosto"
    elif month == 9:
        month_name = "septiembre"
    elif month == 10:
        month_name = "octubre"
    elif month == 11:
        month_name = "noviembre"
    elif month == 12:
        month_name = "diciembre"
    else: 
        return "error"

    return month_name

# month = int(input())
# print(number_to_month(month))