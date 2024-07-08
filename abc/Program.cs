
Console.WriteLine("Введите коэффициенты квадратного уравнения ax^2 + bx + c = 0:");

Console.Write("Введите a: ");
double a = Convert.ToDouble(Console.ReadLine());

Console.Write("Введите b: ");
double b = Convert.ToDouble(Console.ReadLine());

Console.Write("Введите c: ");
double c = Convert.ToDouble(Console.ReadLine());

// Вызов функции для решения уравнения
SolveQuadraticEquation(a, b, c);

Console.ReadLine();


static void SolveQuadraticEquation(double a, double b, double c)
{
    double discriminant = b * b - 4 * a * c;

    if (discriminant > 0)
    {
        double x1 = (-b + Math.Sqrt(discriminant)) / (2 * a);
        double x2 = (-b - Math.Sqrt(discriminant)) / (2 * a);

        Console.WriteLine("Уравнение имеет два корня:");
        Console.WriteLine($"x1 = {x1}");
        Console.WriteLine($"x2 = {x2}");
    }
    else if (discriminant == 0)
    {
        double x = -b / (2 * a);
        Console.WriteLine("Уравнение имеет один корень:");
        Console.WriteLine($"x = {x}");
    }
    else
    {
        Console.WriteLine("Уравнение не имеет действительных корней.");
    }
}
