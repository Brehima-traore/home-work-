immutable_var = 99 ,7, "hi", [8,88],(9<99)
print(immutable_var)
#immutable_var[1] = 45 #'tuple' object does not support item assignment
#print(immutable_var) #'tuple' object does not support item assignment
mutable_list= [99,45,"hi",(9<99),[8,88]]
mutable_list[4] = "ok"
print(mutable_list)