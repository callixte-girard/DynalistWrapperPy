from static import constants as cst

import dynalist


your_file_id = "your_file_id"

dl = dynalist.Dynalist(token=cst.dynalist_token, file_id=your_file_id)
test = dl.get_node("root")
print(test)