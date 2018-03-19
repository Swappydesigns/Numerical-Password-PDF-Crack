#When you have the password = abc you have to call the function decrypt in PyPDF to decrypt the pdf file
import PyPDF2 as pypdf
import sys
import subprocess
filePath ="5020XXXXXX7403_c34a819c_10Feb2018_TO_09Mar2018_052508649.pdf"
f = pypdf.PdfFileReader(open(filePath, "rb"))
output = pypdf.PdfFileWriter()

decode_status = "Couldn't be decoded"

# Assuming 8 digit password with first digit starting from 1.
for i in range(10000000, 99999999):
	if i%100==0: print(i)
	try:
		f.decrypt (str(i))
		# Copy the pages in the encrypted pdf to unencrypted pdf with name noPassPDF.pdf
		for pageNumber in range (0, f.getNumPages()):
		   output.addPage(f.getPage(pageNumber))
		   # write "output" to noPassPDF.pdf
		   outputStream = open(str(i)+"-noPassPDF.pdf", "wb")
		   output.write(outputStream)
		   outputStream.close()
		decode_status = "Decoded Successfully with password " + str(i)
		break
	except pypdf.utils.PdfReadError:
		#print("password incorrect")
		pass
print(decode_status)
# #Open the file now
#    if sys.platform.startswith('darwin'):#open in MAC OX
#       subprocess.call(["open", "noPassPDF.pdf"])
