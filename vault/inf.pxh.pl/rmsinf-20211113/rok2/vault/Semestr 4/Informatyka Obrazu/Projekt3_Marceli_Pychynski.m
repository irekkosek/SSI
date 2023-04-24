%% Zadanie 1
% 
I = imread("cameraman.tif");
Ii = im2uint8(I);
h = fspecial('average') %3x3, zawiera juz wage filtra to samo co h=[ 1/9, ...

h = fspecial('average', [5, 5]) % 5x5

Fa=imfilter(Ii, fspecial('average'), 'replicate');
Fb=imfilter(Ii, fspecial('average'), 'symmetric');
Fc=imfilter(Ii, fspecial('average'), 'circular');
%Fd=imfilter(Ii, fspecial('average'), numeric scalar,X);
Fd=imfilter(Ii, fspecial('average'), 3);
subplot(1,5,5);
subplot(1,5,1);
imshow(Ii);
subplot(1,5,2);
imshow(Fa);
subplot(1,5,3);
imshow(Fb);
subplot(1,5,4);
imshow(Fc);
subplot(1,5,5);
imshow(Fd);

%Replicate i symmetric są do siebie podobne, reszta posiada całkowicie
%inne brzegi


Da=imfilter(Ii, fspecial('average', [5, 5]), 'replicate');
Db=imfilter(Ii, fspecial('average', [5, 5]), 'symmetric');
Dc=imfilter(Ii, fspecial('average', [5, 5]), 'circular');
Dd=imfilter(Ii, fspecial('average', [5, 5]), 3);

figure(2);
subplot(2,5,1);
imshow(Ii);
subplot(2,5,2);
imshow(Da);
subplot(2,5,3);
imshow(Db);
subplot(2,5,4);
imshow(Dc);
subplot(2,5,5);
imshow(Dd);

%Znowu podobnie wyglądają warunki 'replicate' i 'symmetric' warunki te
%różnią się tym, że symmetric tworzy odbicie lustrzane, a replicate
%powtorza wartości, z tego moze wynikac podobienstwo na krawędziach

%%  Zadanie 2

I = imread("cameraman.tif");
Ii = im2uint8(I);

Ca=imfilter(Ii, fspecial('average'), 0);
Cb=imfilter(Ii, fspecial('average'), 0);
Cb=conv2(Ii, fspecial('average'), 'full'); %bialy obrazek :/

%% Zadanie 3

I = imread('cameraman.tif');
N = imnoise(I, 'gaussian', 0.001, 0);

h1 = fspecial('gaussian', [3 3], 3);
h2 = fspecial('gaussian', [7 7], 3);


figure(3);
subplot(1,4,1); imshow(I);
subplot(1,4,2); imshow(N);
subplot(1,4,3); imshow(imfilter(I,h1));
subplot(1,4,4); imshow(imfilter(I,h2));

%% Zadanie 4

I = imread('cameraman.tif');

N = imnoise(I, 'salt & pepper', 0.01);

D1 = medfilt2(N, [3 3]);
D2 = medfilt2(N, [5 5]);

figure(4);
subplot(2,2,1); 
imshow(I);
subplot(2,2,2); 
imshow(N);
subplot(2,2,3); 
imshow(D1);
subplot(2,2,4); 
imshow(D2);

%% Zadanie 5