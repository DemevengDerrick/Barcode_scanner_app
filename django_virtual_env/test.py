import requests

def get_Form_id():
    rq = requests.get("https://esurv.afro.who.int/api/v1/forms", auth=("training_gis", "training_gis")).json()

    #supervision_forms_names = ["Environmental Surveillance Collection Supervision Form","Formulário de supervisão de vigilância ambiental: Moçambique", "Environmental Surveillance Surveillance Supervisory Checklist BURKINA FASO", "Environmental Surveillance Surveillance Supervisory Checklist","Environmental Surveillance Collection Supervision Form BENIN"]
    form_id = []

    for i in rq:
        if i["title"].startswith("Environmental Surveillance Collection Supervision Form") or i["title"].startswith("Formulário de supervisão de vigilância ambiental") or i["title"].startswith("Environmental Surveillance Surveillance Supervisory Checklist"):
            form_id.append(i["formid"])
    print(form_id)
    return form_id

get_Form_id()