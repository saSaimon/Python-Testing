# IteminChart = 0
# if IteminChart != 2:
#     pass
#     # raise Exception("Condition doesnt match")
#     assert(IteminChart == 0)

# try:
#     with open("test.txt", "r") as reader:
#         reader.read()
# except:
#     print("Test Case fails")

try:
    with open("saimon.txt","r") as reader1:
        reader1.read()
except Exception as e:
    print(e)