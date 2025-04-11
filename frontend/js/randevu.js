document.getElementById('appointmentForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const date = document.getElementById('date').value;
    const service = document.getElementById('service').value;
    
    // Burada backend'e randevu bilgilerini göndereceğiz
    console.log('Randevu bilgileri:', { name, email, date, service });
    
    alert('Randevunuz alındı! Teşekkür ederiz.');
    this.reset();
});