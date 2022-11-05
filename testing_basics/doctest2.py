def compruebamail(mailUsuario):
    """
    La función comprueba si se ingresa un usuario con 
    un solo @, de lo contrario es incorrecto.
    
    >>>compruebamail('mecomontes@gmail.com')
    True
    
    >>>compruebamail('meco.mail@')
    False

    >>>compruebaemail('asad@aslkf@.c')
    False

    >>>compruebaemail('asfklns')
    False

    """
    arroba = mailusuario.count('@')
    return (
        arroba == 1
        and mailusuario.rfind('@') != len(mailusuario) - 1
        and mailusuario.find('@') != 0
    )

