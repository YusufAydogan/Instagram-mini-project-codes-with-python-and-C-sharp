
namespace Atm_app

{
    class Program
    {
        static void Main(string[] args)
        {
            int bakiye = 1000;
            Console.WriteLine("ATM'ye Hoşgeldiniz");
            Console.WriteLine("Lutfen Seciminizi yapınız");
            Console.WriteLine("1:Bakiye Gorüntüleme   2:Para Yatırma  3: Para Çekme    4: Çıkış");
            string secim = Console.ReadLine();

            if (secim == "1")
            {
                Console.WriteLine("Bakiyeniz:" +bakiye);
                Console.ReadLine();

            }

            else if (secim == "2")
            {
                Console.WriteLine("Yatırmak İstediğiniz Miktarı Yazınız");
                int yatırma =Convert.ToInt32(Console.ReadLine());

                Console.WriteLine("Yatırılan Tutar:"+yatırma);
                Console.WriteLine("İslem Bassarıyla Gerceklesti");
                Console.WriteLine("Yeni Bakiye:"+((bakiye) + (yatırma)));
            }

            else if (secim == "3")
            {
                Console.WriteLine("Cekmek İstediğiniz Miktarı Yazınız");
                string cekme = Console.ReadLine();
                int cekme2 = Convert.ToInt32(cekme);
                if (cekme2 < 1000)
                {
                    Console.WriteLine("Cekilen Tutar:" + cekme);
                    Console.WriteLine("İslem Basarıyla Gerceklesti");
                    Console.WriteLine("Geriye Kalan:"+((bakiye) - (cekme2)));
                }

                else
                {
                    Console.WriteLine("Yetersiz Bakiye");
                }

            }

            else if(secim=="4")
            {
                Console.WriteLine("ATM den Çıkış Yapılıyor");
                Console.WriteLine("Cıkıs Yapıldı İyi Gunler...");
            }

            else
            {
                Console.WriteLine("Lütfen Geçerli Bir Deger Giriniz");
            }
            Console.ReadLine();

        }
    }
}
