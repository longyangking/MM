x = 8:0.2:12;
y = real(1-(10^2)./(x.^2-10^2+i*0.2*x));
plot(x,y,'k*')
hold on

xi = 0:0.1:20;
y1 = interp1(x,y,xi,'linear');
y2 = interp1(x,y,xi,'spline');
y3 = interp1(x,y,xi,'cubic');
y4 = interp1(x,y,xi,'v5cubic');
y5 = interp1(x,y,xi,'nearest');

plot(xi,y1,'b-')
plot(xi,y2,'m--')
plot(xi,y3,'c.-')
plot(xi,y4,'g:')
plot(xi,y5,'r+')
legend('raw data','linear','spline','cubic','polyfit')
hold off;

