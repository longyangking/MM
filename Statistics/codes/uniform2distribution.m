numofpoints = 200; numofsamples = 100;

samples = rand(numofsamples, numofpoints);
data = mean(samples,2);
mu = mean(data);
sigma = std(data);

pd = makedist('Normal','mu',mu,'sigma',sigma);
xmin = 0.25; xmax = 0.75;
x = xmin:(xmax-xmin)/1000:xmax;
pdf_normal = pdf(pd,x);

hold on;
hist(data);
plot(x,pdf_normal,'LineWidth',2,'Color','r');
xlim([xmin,xmax]); title('Normal Distribution');
hold off;