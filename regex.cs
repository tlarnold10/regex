using System;
using System.Text.RegularExpressions;
using System.Threading;

class Program
{
    static void Main()
    {
        string input = "Kendra is the mom, trevor is the dad, winnie is the puppy and sydney is the baby";
    
        // ^ Matches beginning of line
        string output = Regex.Replace(input, "^Kendra", "k gerber");

        // Write the output.
        Console.WriteLine(input);
        Console.WriteLine(output);


        string input1 = "ohh ehh ohhhh ahh ahh";

        // Match 2 amount of times or more
        string output1 = Regex.Replace(input1, "h{2,}", "h");

        // Write the output.
        Console.WriteLine(input1);
        Console.WriteLine(output1);

        // Sleep for a bit to actually see the output
        Thread.Sleep(9000);
    }
}