# CSV-Compressor
Hoe it works? let’s assume we have the next data:

        1,666,A,0 ...
        2,667,A,0 ...
        3,668,B,0 ...
        1,669,B,0 ...

We will apply the next algorithm on the CSV file.

   #1. Insert the data into containers. Each appearance of data will be inserted once. for example:

        cont0 = [ ‘1’, ‘2’, ‘3’] // ‘1’ referenced below by index 0, ‘2’ referenced below by index 1 etc.
        cont1 = [ '666', '667', '668', '669' ]
        cont2 = [ 'A','B' ]
        cont3 = [ '0' ] // ‘0’ only one because there is one appearance
        ….


   #2. The data will be inserted to the compressed file in the next manner:

        1,2,3@ // ‘@’ will mark end of container
        666,667,668,669@
        A,B@
        0
        @@@ // ‘@@@’ will mark the end of containers part
        &0,1,0,0&1,2,0,0&2,3,1,0,&0,4,1,0, //’&’ will mark beginning of a row. Each row contains the key index
