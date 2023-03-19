#Andrejs Vasiljevs 12 grupa 221RDB441

def build_heap(data):
    
    swaps = []
    length = len( data )
    
    for i in range( length // 2, -1, -1 ):
        
        cnt = i
        
        while True:
            
            maxI = cnt
            rightC = 2 * cnt + 2    
            leftC = 2 * cnt + 1
            
            if rightC < length and data[ rightC ] < data[ maxI ]:
                
                maxI = rightC
            
            if leftC < length and data[ leftC ] < data[ maxI ]:
                
                maxI = leftC
                
            if cnt != maxI:
                
                swaps.append( i, maxI )
                data[ cnt ], data[ maxI ] = data[ maxI ], data[ cnt ]
                
                cnt = maxI
                rightC = 2 * cnt + 2
                leftC = 2 * cnt + 1
                
            else:
                
                break
            
    return swaps

def main():
    
    check = input()
    
    if "I" in check:
        
        length = int( input() )
        data = list( map( int, input().split() ))
            
    if "F" in check:
       
       path =  './tests/'
       file = input()
       filepath = path + file
       
       if "a" not in file:
           
            try:
                
               with open( filepath ) as f:
                   
                length = int( f.readline() )
                data = list( map( int, f.readline().split() ))
                   
            except Exception as o:
               
               print( "File not found") 
               
               return
           
       else:
           
        print( "Error" )


    assert len(data) == length

    swaps = build_heap(data)
    
    assert len(swaps) <= length * 4

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
