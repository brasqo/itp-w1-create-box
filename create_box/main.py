"""This is the entry point of the program."""
#Done with Paige and Tara


def create_box(height, width, character):
    if height < 1 and width < 1:
        return "Both height and width are incorrect"
    elif height < 1:
        return 'Height is less than 1'
    elif width < 1:
        return 'Width is less than 1'
    if not isinstance (character, str):
        return 'Character is not a string'

    mybox = ''
    for i in range(height): 
        charizard = ''
        for j in range(width):
            charizard += character
        mybox += charizard + '\n'
        
    return mybox


    
def empty_box(height, width, character):
    if height < 1:
        return 'Height is less than 1'
    if width < 1:
        return 'Width is less than 1'
    if not isinstance (character, str):
        return 'Character is not a string'
    
    mybox = ''
    for i in range(height): 
        charizard = ''
        for j in range(width):
            # Only add character if its at the end points
            if i == 0 or j == 0 or i == (height - 1) or j == (width - 1):
                charizard += character
            else:
                charizard += ' '        
        mybox += charizard 
        mybox += '\n'

    return mybox
    

if __name__ == '__main__':
    print(create_box(3, 4, '*'))
    print(create_box(0, 3, '#'))
    print(create_box(3, 0, '$'))
    print(create_box(3, 4, 3))
    print(empty_box(3, 4, '*'))
    print(empty_box(0, 3, '#'))
    print(empty_box(3, 0, '$'))
print(empty_box(3, 4, 3))
