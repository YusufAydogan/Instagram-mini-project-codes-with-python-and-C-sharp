class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Lütfen kilonuzu giriniz:");
            double kilo = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Lütfen boyunuzu giriniz:");
            double boy = Convert.ToDouble(Console.ReadLine());

            double boy2 = boy * boy;
            double endeks = kilo / boy2;

            if (endeks <= 18)
            {
                Console.WriteLine("Beden - Kitle Endeksi: " + endeks + "(ZAYIF)");
            }

            else if (endeks > 18 && endeks < 25)
            {
                Console.WriteLine("Beden - Kitle Endeksi: " + endeks + "(NORMAL)");
            }

            else if(endeks > 25)
            {
                Console.WriteLine("Beden - Kitle Endeksi: " + endeks + "(OBEZ)");
            }

            Console.ReadLine();
        }   
             
    }
}
