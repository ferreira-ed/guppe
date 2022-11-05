"""
Estruturas condicionais

if (se), else (senão), elif (else if, senão se)

Exemplo de if em C#
if(idade < 18){
    Console.WriteLine("Menor de idade");
}else if(idade == 18){
    Console.Writeline("Tem 18 anos");
}else{
    Console.WriteLine("Maior de idade");
}

"""

idade = 18

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Tem 18 anos')
else:
    print('Maior de idade')


