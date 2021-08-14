from plyer import notification
import requests



def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="F:\Python files\Project\covid notification system\icon.ico",
        timeout=5,
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    url = "https://www.mohfw.gov.in/data/datanew.json"
    data = requests.get(url).json()

    my_dict = {}
    for dict in data:
        my_dict[dict["state_name"]] = dict

    v = []

    def print_info(state):
        info = my_dict[state]
        val = list(info.values())
        v.append(val[1])
        v.append(val[6])
        v.append(val[8])
        v.append(val[9])

    print_info("Odisha")  # here we can put ant states name

    nTitle = "Cases of Covid-19"
    nText = f"State : {v[0]}\nActive : {v[1]}\nCured : {v[2]}\nDeath : {v[3]}"
    notifyMe(nTitle, nText)




