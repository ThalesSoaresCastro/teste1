#menor priority => maior prioridade
#Gere 2 arquivos de saída, watchers.json e manager.json. 
import json
data = []
merlin_m = []
csa_m = []
merlin_w = []
morris_w =[]

with open("source_file_2.json", "r") as json_file:
    
    data = json.load(json_file)

for d in data:
    for m in d['managers']:
        if m == 'merlin':
            merlin_m.append(([d['name'], d['priority']]))
        if m == 'csaftoiu':
            csa_m.append((d['name'], d['priority']))
    for w in d['watchers']:
        if(w == 'merlin'):
            merlin_w.append(([d['name'], d['priority']]))
        else:
            morris_w.append(([d['name'], d['priority']]))


#ordena pela prioridade...
csa_m_Rev = sorted(csa_m, key=lambda csa: csa[1], reverse=True)
merlin_m_Rev= sorted(merlin_m, key=lambda mrl_m: mrl_m[1], reverse=True)
merlin_w_Rev = sorted(merlin_w, key=lambda mrl_w: mrl_w[1], reverse=True)
morris_w_Rev= sorted(morris_w, key=lambda mor_w: mor_w[1], reverse=True)

def list_data(tpl_dt):
    lst_tp = []
    for tp in tpl_dt:
        lst_tp.append(tp[0])
    return lst_tp

def salvar_json_w(data):
    with open('watchers.json', 'w') as f:
        json.dump(data, f)



def salvar_json_m(data):
    with open('managers.json', 'w') as f:
        json.dump(data, f)


#managers
#print({"csaftoiu":list_data(csa_m_Rev),"merlin":list_data(merlin_m_Rev)})
salvar_json_m({"csaftoiu":list_data(csa_m_Rev),"merlin":list_data(merlin_m_Rev)})

#watchers
#print({"merlin":list_data(merlin_m_Rev),"morris":list_data(morris_w_Rev)})
salvar_json_w({"merlin":list_data(merlin_m_Rev),"morris":list_data(morris_w_Rev)})
