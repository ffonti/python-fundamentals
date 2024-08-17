#Datetime
import datetime

x = datetime.datetime(2021, 6, 13)
print(x) #2021-06-13 00:00:00

x = datetime.datetime.now()
print(x) #2021-07-29 15:45:00.000000

#%a - Nome del giorno della settimana abbreviato.
#%A - Nome completo del giorno della settimana.
#%w - Giorno della settimana come numero (0-6, dove 0 è domenica).
#%d - Giorno del mese come numero decimale (01-31).
#%b - Nome del mese abbreviato.
#%B - Nome completo del mese.
#%m - Mese come numero decimale (01-12).
#%y - Anno senza secolo come numero decimale (00-99).
#%Y - Anno con secolo come numero decimale.
#%H - Ora (24 ore) come numero decimale (00-23).
#%I - Ora (12 ore) come numero decimale (01-12).
#%p - AM o PM.
#%M - Minuti come numero decimale (00-59).
#%S - Secondi come numero decimale (00-59).
#%f - Microsecondi come numero decimale (000000-999999).
#%z - Offset del fuso orario in formato +HHMM o -HHMM.
#%Z - Nome del fuso orario.
#%j - Giorno dell'anno come numero decimale (001-366).
#%U - Numero della settimana dell'anno (domenica come primo giorno della settimana) come numero decimale (00-53).
#%W - Numero della settimana dell'anno (lunedì come primo giorno della settimana) come numero decimale (00-53).
#%c - Rappresentazione locale della data e dell'ora.
#%x - Rappresentazione locale della data.
#%X - Rappresentazione locale dell'ora.
#%% - Un carattere di percentuale letterale (%).

print(x.strftime("%A")) #Thursday

print(x.strftime("%d/%m/%Y")) #17/08/2024