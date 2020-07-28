def Howbad(land):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    # Mache das plot erst bei plt.show() zeigt
    plt.interactive(False)
    landnam = str(land)
    # Lade aktuelle Daten herunter
    corona = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/full_data.csv")
    # mache log
    corona = pd.DataFrame(corona)
    # Filtere nur Tage welche fälle != 0
    corona = corona[corona["total_cases"] != 0]
    # Füge log Achse hinzu
    corona["total_cases_log"] = corona["total_cases"].apply(np.log)
    # Filter Dataframe nach land daten
    Land = corona[corona["location"] == landnam]
    # Filtere nur Tage welche fälle != 0
    Land = Land[Land["total_cases"] != 0]
    # Plote 2 subplots mit cases log und ohne
    fig, (mitlog, ohnelog) = plt.subplots(2)
    fig.suptitle('Total Cases of ' + landnam)
    mitlog.plot(Land["date"], Land["total_cases_log"])
    mitlog.set_ylabel("Log Cases")
    mitlog.set_xticks([0, len(Land) / 2, len(Land) - 1])
    ohnelog.set_ylabel("Cases")
    ohnelog.plot(Land["date"], Land["total_cases"])
    ohnelog.set_xticks([0, len(Land) / 2, len(Land) - 1])
    plt.show()



