using System.IO;
using System.Security.Cryptography;
using System.Text;

public class SaveLoadManager
{
    private static string key = "A632GHT35W";

    public static void SaveData(string fileName, string data)
    {
        byte[] encryptedData = EncryptString(data, key);

        // Combine the current directory with the file name and extension
        string filePath = Path.Combine(Directory.GetCurrentDirectory(), fileName + ".VIRT");

        // Write the encrypted data to the file
        File.WriteAllBytes(filePath, encryptedData);
    }

    public static string LoadData(string fileName)
    {
        // Combine the current directory with the file name and extension
        string filePath = Path.Combine(Directory.GetCurrentDirectory(), fileName + ".VIRT");

        // If the file exists, load its contents and decrypt it
        if (File.Exists(filePath))
        {
            byte[] encryptedData = File.ReadAllBytes(filePath);
            string decryptedData = DecryptString(encryptedData, key);
            return decryptedData;
        }
        else
        {
            return null;
        }
    }

    private static byte[] EncryptString(string data, string key)
    {
        byte[] keyBytes = Encoding.UTF8.GetBytes(key);
        byte[] dataBytes = Encoding.UTF8.GetBytes(data);

        using (Aes aes = Aes.Create())
        {
            aes.Key = keyBytes;
            aes.GenerateIV();

            using (MemoryStream ms = new MemoryStream())
            {
                ms.Write(aes.IV, 0, aes.IV.Length);

                using (CryptoStream cs = new CryptoStream(ms, aes.CreateEncryptor(), CryptoStreamMode.Write))
                {
                    cs.Write(dataBytes, 0, dataBytes.Length);
                }

                byte[] encryptedData = ms.ToArray();
                return encryptedData;
            }
        }
    }

    private static string DecryptString(byte[] encryptedData, string key)
    {
        byte[] keyBytes = Encoding.UTF8.GetBytes(key);

        using (Aes aes = Aes.Create())
        {
            aes.Key = keyBytes;

            byte[] iv = new byte[aes.IV.Length];
            Array.Copy(encryptedData, iv, iv.Length);
            aes.IV = iv;

            using (MemoryStream ms = new MemoryStream())
            {
                using (CryptoStream cs = new CryptoStream(ms, aes.CreateDecryptor(), CryptoStreamMode.Write))
                {
                    cs.Write(encryptedData, iv.Length, encryptedData.Length - iv.Length);
                }

                byte[] decryptedData = ms.ToArray();
                return Encoding.UTF8.GetString(decryptedData);
            }
        }
    }
}
