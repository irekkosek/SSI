%% Zadanie 1
I = imread("pout.tif");
typ = class(I);
L = min(typ);
H = max(typ);
[r,c] = size(I);
imshow(I)
title(I,imfinfo('pout.tif').ImageDescription);
%% Zadanie 2
Ii = imread('pout.tif');
Id = im2double(Ii);

subplot(2,2,1);
imshow(Ii);
title('uint8');

subplot(2,2,2);
imshow(Id);
title('double');

subplot(2,2,3);
histogram(Ii);

subplot(2,2,4);
histogram(Id);
%% Zadanie 3
figure(1)

subplot(1,3,1);
imhist(I)

subplot(1,3,2);
imhist(Id)

subplot(1,3,3);
imhist(Ii)
figure(2)

subplot(2,3,1);
imshow(I)

subplot(2,3,2);
imshow(Id)

subplot(2,3,3);
imshow(Ii)

subplot(2,3,4);
histogram(I)

subplot(2,3,5);
histogram(Id)

subplot(2,3,6);
histogram(Ii)

%% Zadanie 4
figure(1);
n = 50;
subplot(2,3,1);
imshow(I);
title('Orginalny');

subplot(2,3,2);
imshow(I+n);
title('+');

subplot(2,3,3);
imshow(I-n);
title('-');

subplot(2,3,4);
histogram(I)

subplot(2,3,5);
histogram(I+n);

subplot(2,3,6);
histogram(I-n);

figure;
m = 150;

subplot(2,3,1);
imshow(I);
title('Orginalny')

subplot(2,3,2);
imshow(I+m);
title('+');

subplot(2,3,3);
imshow(I-m);
title('-');

subplot(2,3,4);
histogram(I)

subplot(2,3,5);
histogram(I+m);

subplot(2,3,6);
histogram(I-m);

%% Zadanie 5

M1 = imadjust(Ii,[0.0,0.5],[]);
M2 = imadjust(Ii,[0.5,1.0],[]);

figure(1);
subplot(2,3,1);
imshow(Ii);

subplot(2,3,2);
imshow(M1);

subplot(2,3,3);
imshow(M2);


subplot(2,3,4);
histogram(I)

subplot(2,3,5);
histogram(M1);

subplot(2,3,6);
histogram(M2);
%% Zadanie 6
D = imadjust(Id,[0.0,1.0],[0.0,0.3]);
C = imadjust(Id,[0.0,1.0],[0.7,1.0]);

figure(1);
subplot(2,3,1);
imshow(Ii);

subplot(2,3,2);
imshow(D);

subplot(2,3,3);
imshow(C);


subplot(2,3,4);
histogram(I)

subplot(2,3,5);
histogram(D);

subplot(2,3,6);
histogram(C);
%% Zadanie 7
imwrite(M1,"M1.tif")
imwrite(M2,"M2.tif")
imwrite(D,"D.tif")
imwrite(C,"C.tif")