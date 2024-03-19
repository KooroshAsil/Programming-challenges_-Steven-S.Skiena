n_days = 100
n_parties = 4
hps = [12,15,25,40]

table = {}
days = {0: "Su", 1: "Mo", 2: "Tu", 3: "We", 4: "Th", 5: "Fr", 6: "Sa"}
calendar = {}
paday = [[] for _ in range(len(hps))]

for d in range(n_days):
    table[d] = False
    calendar[d] = days[d % 7]

for i, p in enumerate(hps):
    l = paday[i]
    for d in range(p - 1, n_days, p):
        l.append(d)

number_loss = 0
intersections = []

for i, ds1 in enumerate(paday):
    for ds2 in paday[i + 1:]:
        intersect = set(ds1).intersection(ds2)
        if intersect and intersect not in intersections:
            intersections.append(intersect)

for inter in intersections:
    for i, ds in enumerate(paday):
        if inter.intersection(ds):
            for day in inter.intersection(ds):
                if calendar[day] != "Fr" and calendar[day] != "Sa":
                    paday[i].remove(day)

for i in range(len(paday)):
    paday[i] = [element for element in paday[i] if element not in intersections]

number_loss += len(intersections)   

for i, p in enumerate(hps):
    l = paday[i]
    for d in l:
        if calendar[d] == "Fr" or calendar[d] == "Sa":
            pass
        else:
            number_loss += 1

print("Number of working days lost:", number_loss)