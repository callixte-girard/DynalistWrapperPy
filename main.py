from static import constants as cst

import dynalist


dl = dynalist.Dynalist(token=cst.dynalist_token, file_id='4QqbACmY8arqQeSa8bt_TZqP')
test = dl.get_node("root")
print(test)