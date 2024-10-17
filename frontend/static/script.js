document.querySelector('form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const field = e.target.field.value;
    const response = await fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ field })
    });
    const data = await response.json();
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '<ul>' + data.ideas.map(idea => `<li>${idea}</li>`).join('') + '</ul>';
});
