mathmk = int( input( "What was your maths mark?: " ))
chemmk = int( input( "What was your chemistry mark?: " ))
phymk = int( input( "What was your physics mark?: " ))
overall_grade = mathmk + chemmk + phymk

print( mathmk, "+", chemmk, "+", phymk, "=", overall_grade )

percentage = str( float( (overall_grade / 300 ) * 100 ))+'%'

print(percentage)

if percentage < '50' :
    print( "D" )
elif percentage < '60' :
    print( "C" )
elif percentage < '70' :
    print( "B" )
else :
    print( "A!" )
