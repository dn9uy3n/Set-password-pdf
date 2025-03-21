# pdf_encryptor.py
import sys
import pikepdf

def encrypt_pdf(input_path, output_path, password):
    try:
        pdf = pikepdf.open(input_path)
        pdf.save(output_path, encryption=pikepdf.Encryption(owner=password, user=password, R=4))
        print(f"✅ PDF đã được mã hóa và lưu tại: {output_path}")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Cách dùng: python pdf_encryptor.py <input.pdf> <output.pdf> <password>")
    else:
        encrypt_pdf(sys.argv[1], sys.argv[2], sys.argv[3])
