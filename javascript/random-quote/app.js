const quotes = ["Stay curious.", "Measure twice, cut once.", "Small scripts, sharp skills."];
document.getElementById('b').onclick = () => {
  document.getElementById('q').textContent =
    quotes[Math.floor(Math.random()*quotes.length)];
};
