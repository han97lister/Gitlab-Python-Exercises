#word1 = input( "Enter first word: ")
#word2 = input( "Enter second word: ")

def near( string_big, string_small ) :

    list_big = list( string_big )
    list_small = list( string_small )

    for index in range( len( list_big )) :
        
        item_to_remove = list_big[ index ]
        del list_big[ index ] #del deletes indices in lists

        if list_big == list_small :
            return True
        
        list_big.insert( index, item_to_remove ) #insert adds other indices back
    
    return False

#print( near( word1, word2 ) )