%% Zadanie 1
I = imread("pout.tif");
typ = class(I)
L = min(I,[],"all")
H = max(I, [], "all")
rozmiar = size(I);
r = rozmiar(1)
c = rozmiar(2)
opis = imfinfo("pout.tif").ImageDescription
figure(6)
imshow(I)
title(I, opis);

%% Zadanie 2
Ii = im2uint8(I);
Id = im2double(I);
Ii = imadjust(Ii, stretchlim(Ii),[0 1]);
Id = imadjust(Id, stretchlim(Id), [0 1]);
figure(1)
subplot(1,2,1);
imshow(Id);
title("double");
subplot(1,2,2);
imshow(Ii);
title("uint8");

%% Zadanie 3
figure(2)
subplot(2,3,1)
imshow(I);
subplot(2,3,2);
imshow(Ii);
subplot(2,3,3);
imshow(Id);
subplot(2,3,4);
imhist(I);
subplot(2,3,5);
imhist(Ii);
subplot(2,3,6);
imhist(Id);
% Uzyskane histogramy nie są identyczne. Pierwszy różni się od pozostałych
% tym, że jest histogramem obrazu nieznormalizowanego, stąd histogram nie 
% jest "rozciągnięty" na cały zakres wartości. Kolejne dwa histogramy 
% różnią się między sobą skalą na osi X, dla histogramu obrazu typu
% uint8 jest to skala 0-255, a dla histogramu obrazu typu double jest
% to skala 0-1.
figure(3)
subplot(2,3,1)
imshow(I);
subplot(2,3,2);
imshow(Ii);
subplot(2,3,3);
imshow(Id);
subplot(2,3,4);
histogram(I, "Normalization", "probability");
subplot(2,3,5);
histogram(Ii, "Normalization", "probability");
subplot(2,3,6);
histogram(Id, "Normalization", "probability");

%%Zadanie 4
wartosc = 30;
figure(4)
subplot(2,3,1)
imshow(I);
subplot(2,3,2);
imshow(I+wartosc);
subplot(2,3,3);
imshow(I-wartosc);
subplot(2,3,4);
imhist(I);
subplot(2,3,5);
imhist(I+wartosc);
subplot(2,3,6);
imhist(I-wartosc);

wartosc2 = 130;
figure(5)
subplot(2,3,1)
imshow(I);
subplot(2,3,2);
imshow(I+wartosc2);
subplot(2,3,3);
imshow(I-wartosc2);
subplot(2,3,4);
imhist(I);
subplot(2,3,5);
imhist(I+wartosc2);
subplot(2,3,6);
imhist(I-wartosc2);

%Po dodaniu pewnej wartosci do obrazu rozjaśnia się on, a po odjęciu -
%ściemnia. Histogramy przy dodaniu wartości "przesuwają się" w prawo po osi X, 
%a po odjęciu - w lewo. Przy dodaniu mniejszej wartości zmiany są nieco
%bardziej subtelne, po dodaniu sporej wartości - nad wyraz zauważalne.
