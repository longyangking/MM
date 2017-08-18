% The basic game rule: 
%       Pick one person randomly to give 1 property. After giving property, this person will have increased
%       probability to be picked in next round.
% The result: 
%       Non-uniform distribution of property after enough generations

numofpeoples = 100; generations = 10000;

peoples = zeros(1,numofpeoples);
choices = 1:numofpeoples;

for generation = 1:generations
    numofchoices = length(choices);
    choice = randi(numofchoices);
    peoples(choices(choice)) = peoples(choices(choice)) + 1;
    choices = [choices,choices(choice)];
end

figure(1);
bar(peoples); xlim([1,100]);

figure(2);
bar(sort(peoples)); xlim([1,100]);