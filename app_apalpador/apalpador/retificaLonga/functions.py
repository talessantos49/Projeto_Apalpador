import gspread
import sys, datetime
import statistics as st
import pandas as pd

gc = gspread.service_account(filename='../../service_account.json')
sh = gc.open_by_key('1noVM0ci_yNDi7I2egsF2-erzuTgBLa9LrOrM4q96xCk')
worksheet = sh.worksheet("Página1")

# Quais valores eu preciso?
# - Quantidade de peças por dia(data); --- CHECKED
# - Quantidade de peças por Maquina; --- CHECKED
# - Quantidade de peças por Turno 06:00 as 14:00 - 14:00 as 22:00 - 22:00 as 06:00; --- CHECKED

# - Tempo da Ultima peça; --- CHECKED
# - Tempo médio das peças; --- CHECKED
# - Tempo médio ocioso;
# - Tempo total Ocioso do Dia(data); 

def media_data_input() :
    received_values = {}
    received_values = worksheet.get_all_records()
    print(received_values[-1]["Horário"])
    print(received_values[-1]["Data"])
    date_segregation()

def actual_date():
    today = datetime.date.today()
    data = str(today)
    data = data.split('-')
    str_data = []
    str_data.append(data[2])
    str_data.append(data[1])
    str_data.append(data[0])
    str_data = '/'.join(str_data)
    return(str_data)

def date_segregation() :
    # all_data = worksheet.get_all_records()
    all_values = worksheet.get_all_values()
    print("A data atual é: " + str(actual_date()))
    date_actual = str(actual_date())#"24/02/2023" #Só alterar para pegar os valores da actual_date()
    i = 0
    parts_list_timer = []
    actual_timer = []
    turn_parts = 0
    firts_counter = 0
    second_turn_parts = 0
    second_counter = 0
    third_turn_parts = 0
    third_counter = 0
    ununsual_counter = 0
    day_parts = 0
    for data_collum in all_values:
        if date_actual == data_collum[0]:
            actual_timer.append(data_collum[1].split(':'))
            if int(actual_timer[i][0]) >= 6 and int(actual_timer[i][0]) < 14:
                if int(data_collum[4]) == 0:
                    ununsual_counter += 1
                elif int(data_collum[4]) == firts_counter:
                    ununsual_counter += 1
                elif int(data_collum[4]) > firts_counter:
                    parts_list_timer.append(actual_timer[i])
                    firts_counter = int(data_collum[4])
                    turn_parts += 1
                elif int(data_collum[4]) < firts_counter:
                    parts_list_timer.append(actual_timer[i])
                    firts_counter = int(data_collum[4])
                    turn_parts += 1                                             #QUANTIDADE DE PEÇAS POR TURNO
                # print(str(actual_timer[i]) + " - Peças do Primeiro Turno : " + str(turn_parts))
            elif int(actual_timer[i][0]) >= 14 and int(actual_timer[i][0]) < 22:
                if int(data_collum[4]) == 0:
                    ununsual_counter += 1
                elif int(data_collum[4]) == second_counter:
                    ununsual_counter += 1
                elif int(data_collum[4]) > second_counter:
                    parts_list_timer.append(actual_timer[i])
                    second_counter = int(data_collum[4])
                    second_turn_parts += 1
                elif int(data_collum[4]) < second_counter:
                    parts_list_timer.append(actual_timer[i])
                    second_counter = int(data_collum[4])
                    second_turn_parts += 1                                             #QUANTIDADE DE PEÇAS POR TURNO
                # print(str(actual_timer[i]) + " - Peças do Segundo Turno : " + str(second_turn_parts))
            else:
                if int(data_collum[4]) == 0:
                    ununsual_counter += 1
                elif int(data_collum[4]) == third_counter:
                    ununsual_counter += 1
                elif int(data_collum[4]) > third_counter:
                    parts_list_timer.append(actual_timer[i])
                    third_counter = int(data_collum[4])
                    third_turn_parts += 1
                elif int(data_collum[4]) < third_counter:
                    parts_list_timer.append(actual_timer[i])
                    third_counter = int(data_collum[4])
                    third_turn_parts += 1                                             #QUANTIDADE DE PEÇAS POR TURNO
                # print(str(actual_timer[i]) + " - Peças do Terceiro Turno : " + str(third_turn_parts))
            day_parts = turn_parts + second_turn_parts + third_turn_parts              #QUANTIDADE DE PEÇAS POR DIA
            i += 1
    parts_timer(parts_list_timer)
    print("A quantidade de peças produzidas no dia foi : " + str(day_parts))
    print("A quantidade de datas é: {} ".format(i))

def parts_timer(parts_list):
    all_times = []
    yesterday = 0
    for i in range(len(parts_list)):
        yesterday = datetime.datetime(2023,2,20,int(parts_list[i][0]), int(parts_list[i][1]), int(parts_list[i][2]))
        if i > 1 :
            today = datetime.datetime(2023,2,20, int(parts_list[i-1][0]), int(parts_list[i-1][1]), int(parts_list[i-1][2]))
            all_times.append(str(yesterday-today))
    # print(all_times)
    interger_times = []
    interger_times = all_times
    if len(interger_times) > 1:
        print(interger_times[-1])                                                      # TEMPO ULTIMA PEÇA
        intervalo = pd.to_datetime(interger_times, format='%H:%M:%S')
        data_interval = intervalo.mean()
        data_interval = str(data_interval).split()
        print(data_interval[1])
    else:
        interger_times = yesterday
    # return(all_times)

def create_table():
    str_table = """\t
    <tr>
            <td>"""+ 'Marcos' + """</td>
            <td>"""+ 'Longa' +"""</td>
            <td>"""+ 'Maquina 235' +"""</td>
            <td>"""+ 'Manhã' + """</td>
            <td>"""+ '09:00' + """</td>
            <td>"""+ 'Leandro' + """</td>
    </tr>
    """
    return (str_table)

def input_table():
    table_arq = open('/templates/retificaLonga/table.html', 'w')
    html_script = create_table()
    head_html = """<table id="datatablesSimple">
    <thead>
        <tr>
            <th>Operador</th>
            <th>Setor</th>
            <th>Maquina</th>
            <th>Turno</th>
            <th>Horário</th>
            <th>Lider</th>
        </tr>
    </thead>
    <tfoot>
        <tr>
            <th>Operador</th>
            <th>Setor</th>
            <th>Maquina</th>
            <th>Turno</th>
            <th>Horário</th>
            <th>Lider</th>
        </tr>
    </tfoot>
    <tbody>"""
    tail_html = """
            </tbody>
        </table>"""



if __name__ == "__main__":
    media_data_input()
