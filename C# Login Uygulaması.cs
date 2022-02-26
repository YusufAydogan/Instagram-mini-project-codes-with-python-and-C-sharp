class Program
    {
        static void Main(string[] args)
        {
            int hak = 3;

            while (true)
            {
                Console.WriteLine("Lütfen kullanıcı adınızı giriniz:");
                string kullaniciadi = Console.ReadLine();

                Console.WriteLine("Lütfen parolanızı giriniz:");
                string parola = Console.ReadLine();


                if (kullaniciadi == "yusuf" && parola == "123")
                {
                    Console.WriteLine("Giriş Başarılı");
                    break;
                }

                else
                {
                    Console.WriteLine("Yanlış kullanıcı adı veya parola");

                    if (hak>0)
                    {
                        Console.WriteLine("Kalan Hakkınız:" +(hak-=1));
                    }

                    if (hak == 0)
                    {
                        Console.WriteLine("Deneme hakkınız bitti lütfen 5 dakika sonra tekrar deneyiniz");
                        break;
                    }

                }
                Console.ReadLine();
            }
        }   
             
    }
}
