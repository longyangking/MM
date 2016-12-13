x = 8:0.1:12;
wp = 10; w0 = 10; tau = 0.1;
y = 1+wp^2*(w0^2-x.^2)./((w0^2-x.^2).^2+tau^2*x.^2);
plot(x,y,'r+')
hold on

ft = fittype('1+wp^2*(w0^2-x^2)/((w0^2-x^2)^2+tau^2*x^2)');

[curve,gof] = fit(x',y',ft,'StartPoint',[2,10,10]);
%[curve,gof] = fit(x',y',ft);

plot(curve,x,y)

fprintf('######################Fit Result##############################\n');
fprintf('w0 = %f\n',curve.w0)
fprintf('wp = %f\n',curve.wp)
fprintf('tau = %f\n',curve.tau)