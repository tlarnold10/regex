using System;
using System.Text.RegularExpressions;
using System.Threading;

class Program
{
    static void Main()
    {
        string input = "Kendra is the mom, trevor is the dad, winnie is the puppy and sydney is the baby";
    
        string output = Regex.Replace(input, "^Kendra", "k gerber");

        // Write the output.
        Console.WriteLine(input);
        Console.WriteLine(output);
        Thread.Sleep(9000);
    }
}