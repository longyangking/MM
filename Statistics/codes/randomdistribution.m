% To decrease gap between the wealthy and poor

numofpeoples = 100; generations = 10000; alpha = 0.95;

peoples = zeros(1,numofpeoples);
count = ones(1,numofpeoples);
choices = 1:numofpeoples;

for generation = 1:generations
    numofchoices = length(choices);
    choice = randi(numofchoices);
    pick = choices(choice);
    peoples(pick) = peoples(pick) + count(pick);
    choices = [choices,choices(choice)];
    count(pick) = alpha*count(pick);
end

figure(1);
bar(peoples); xlim([1,100]);

figure(2);
bar(sort(peoples)); xlim([1,100]);