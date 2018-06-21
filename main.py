from Compressor import Compressor

def main():
    print "start"
    comp = Compressor("MyFile.csv", 4, ",")
    comp.compress()
	
    comp.decompress("MyCompressedFile.csv")

    print "end"

if __name__ == "__main__":
    main()
