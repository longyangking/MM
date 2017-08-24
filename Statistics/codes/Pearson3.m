numofdata = 20000; numofsamples = 10; numofpoints = 3; 

data = zeros(1,numofdata);
for n = 1:numofdata
    samples = rand(1,numofsamples);
    pos = randi(numofsamples,1,numofpoints);
    data(n) = mean(samples(pos));
end

hist(data); 