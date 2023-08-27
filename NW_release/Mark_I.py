exp_matrix = []
hid_matrix = []

def build_field(wide,high):

    #build exp matrix

    for y in range(high):
        inter_line = []
        for x in range(wide + 1):
            inter_line.append(0)
        exp_matrix.append(inter_line)

    #build hid martix

    for y in range(high+1):
        inter_line = []
        for x in range(wide):
            inter_line.append(0)
        exp_matrix.append(inter_line)

# warn: global velocity update doesn't need accurate iteration，
# but divergence calculation need , this function is designed for
# divergence calculation. -08-26@2:45 A.M
def d_update(index_posi): #index_posi is a list like:[x,y]
    global exp_matrix, hid_matrix

    def d_calc(points):
        pass
    
    x = index_posi[0]
    y = index_posi[1]

    access_point = [exp_matrix[y][x],exp_matrix[y][x+1],hid_matrix[y][x],hid_matrix[y+1][x]]

    d = d_calc(access_point)

    # d update:



    # end d update

    exp_matrix[y][x] = access_point[0]
    exp_matrix[y][x+1] = access_point[1]
    hid_matrix[y][x] = access_point[2]
    hid_matrix[y+1][x] = access_point[3]


    
