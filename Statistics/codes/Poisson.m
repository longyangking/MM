numofsamples = 5000; lambda = 0.8;
L = exp(-lambda); 

samples = zeros(1,numofsamples);
for n = 1:numofsamples
    p = 1; k = 0;
    while p > L 
        k = k + 1;
        p = p*rand();
    end
    samples(n) = k - 1;
end

hist(samples);