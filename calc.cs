using System;
using System.IO;

namespace prototipo_de_calculadora
{
    class Program
    {
        static void Main(string[] args)
        {
        string[] opResult = {"1-Soma","2-Subtração","3-Multiplicação","4-Divisão"};
        Console.WriteLine("Digite o primeiro numero:");
        int n1 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Digite o segundo numero:");
        int n2 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Digite a operação desejada:");
        Console.WriteLine(opResult[0]);
        Console.WriteLine(opResult[1]);
        Console.WriteLine(opResult[2]);
        Console.WriteLine(opResult[3]);
        int operation = Convert.ToInt32(Console.ReadLine());
        if (operation = 1){
            int n3 = n1 + n2;
            Console.WriteLine("o resultado da",opResult[0],"é:",n3);
        }
        if (operation = 2){
           int n3 = n1 - n2;
            Console.WriteLine("o resultado da",opResult[1],"é:",n3);
        }
        if(operation = 3){
          int n3 = n1 * n2;
            Console.WriteLine("o resultado da",opResult[2],"é:",n3);
        }
        if(operation = 4){
           int n3 = n1 / n2;
            Console.WriteLine("o resultado da",opResult[3],"é:",n3);
        }
        else
        {
            Console.WriteLine("Erro: operação não reconhecida");
        }
        }
    }
}
