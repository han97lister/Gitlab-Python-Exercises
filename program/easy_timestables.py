#print out the times tables from 1 to 10 using a loop

def tablesOnetoTen() :
    x = 1
    y = 1
    for x in range( 1, 11 ) :
        print( "Table for {} * ( 1-10 )".format(x) )

        for y in range( 1 , 11 ) :
            print( x * y, end=" " )
        print()

tablesOnetoTen()