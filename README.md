# Enkriptimi dhe Dekriptimi i Mesazheve në Python permes DES algoritmit

##### Ky eshte nje projekt i punuar nga studente te vitit te dyte te Universitetit "Hasan Prishtina"-Fakulteti i Inxhinieris Elektrike dhe Kompjuterike, ne Lenden "Data Security"-Prof.Blerim Rexha dhe Asc.Mergim Hoti.

## Pershkrimi i projektit: 
##### Ne kete repository gjendet kodi ne gjuhen programuese Python per programimin e nje cifti te thjeshte klient/server te cilet komunikojne mes vete me mesazhe te enkriptuara permes DES algoritmit. Klienti dërgon mesazhe të enkriptuara dhe pranon përgjigje të dekriptuara nga serveri.

## Struktura e Projektit

#### Projekti përfshin dy skripta Python:

##### - `server.py`: Kjo është skripta që ekzekuton serverin. Ai pranon lidhje të reja nga klientët dhe pastaj dekripton mesazhet që merr nga ata.
##### - `client.py`: Kjo është skripta që ekzekuton klientin. Përdoruesi mund të jep një mesazh që dëshiron të dërgojë në server për të enkriptuar dhe pastaj ta dërgojë.


## Si të përdorim këtë projekt:
##### Për të përdorur këtë projekt, duhet të keni Pythonin dhe libraritë e nevojshme të instaluar në mjedisin tuaj. Libraria pyDes është e nevojshme për të punuar me algoritmin DES në Python.

##### 1. Fillimisht, sigurohuni që keni instaluar Pythonin në sistemin tuaj.
##### 2.Instaloni libraritë e nevojshme duke përdorur pip. Libraritë që duhen instaluar janë 'pyDes'.
##### 3.Kopjoni kodin e klientit në një skedar të quajtur 'client.py', dhe kodin e serverit në një skedar të quajtur 'server.py'.
##### 4.Ekzekutoni skriptën `server.py` duke shkruar ne terminal: python server.py
##### 5.Pastaj, ekzekutoni 'client.py' në një terminal tjetër ose në një dritare të ndarë, duke shkruar: python client.py.
##### 6.Ndiq instruksionet që i ofron programi.

## Rezultatet e pritshme nga ky projekt janë:

##### Klienti fillon dhe shkruan një mesazh të thjeshtë.
##### Mesazhi i klientit enkriptohet përdorur çelësin e paracaktuar DES.
##### Mesazhi i enkriptuar dërgohet në server.
##### Serveri merr mesazhin e enkriptuar dhe e dekripton duke përdorur të njëjtin çelës.
##### Serveri degon një prompt të enkriptuar tek klienti.
##### Klienti dekripton prompten, merr inputin e userit, e enkripton dhe e kthen te serveri.
##### Në bazë të përgjigjes së user-it serveri kthen prapa mesazhin e enkriptuar ose një mesazh default.


## Kontribues ne kete projekt jane:
##### -[Brikena Kastrati ](https://github.com/brikenakastrati)
##### -[Daris Dragusha ](https://github.com/darisdr)
##### -[Dea Limoni ](https://github.com/DeaLimoni)

