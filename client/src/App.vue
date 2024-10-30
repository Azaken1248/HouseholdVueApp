<template>
  <div class="d-flex flex-column min-vh-100">

    <header class="home-header text-center text-white py-5">
      <h1>Welcome to Household Services</h1>
      <p>Your one-stop solution for all household needs</p>
    </header>

    <div class="container mt-4 flex-grow-1">
      <router-view />
      <div v-if="!$route.name || ($route.name !== 'Login' && $route.name !== 'Registration')" class="row">
        <div class="col-md-4">
          <div class="card text-center text-white bg-base02 mb-4 card-hover">
            <div class="card-body d-flex flex-column justify-content-between" style="height: 300px;">
              <h5 class="card-title">User</h5>
              <i class="fas fa-user-tie fa-3x mb-3"></i>
              <p class="card-text">Login or Register as a user to access household services.</p>
              <div>
                <router-link :to="{ name: 'Login', params: { role: 'User' } }" class="btn btn-outline-primary me-2">Login</router-link>
                <router-link :to="{ name: 'Registration', params: { role: 'User' } }" class="btn btn-outline-primary">Register</router-link>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card text-center text-white bg-base02 mb-4 card-hover">
            <div class="card-body d-flex flex-column justify-content-between" style="height: 300px;">
              <h5 class="card-title">Admin</h5>
              <i class="fas fa-user-shield fa-3x mb-3"></i>
              <p class="card-text">Manage users and services efficiently.</p>
              <div>
                <router-link :to="{ name: 'Login', params: { role: 'Admin' } }" class="btn btn-outline-primary me-2">Login</router-link>
                <router-link :to="{ name: 'Registration', params: { role: 'Admin' } }" class="btn btn-outline-primary">Register</router-link>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card text-center text-white bg-base02 mb-4 card-hover">
            <div class="card-body d-flex flex-column justify-content-between" style="height: 300px;">
              <h5 class="card-title">Service Professional</h5>
              <i class="fas fa-user-cog fa-3x mb-3"></i>
              <p class="card-text">Join as a professional to offer your services.</p>
              <div>
                <router-link :to="{ name: 'Login', params: { role: 'Service Professional' } }" class="btn btn-outline-primary me-2">Login</router-link>
                <router-link :to="{ name: 'Registration', params: { role: 'Service Professional' } }" class="btn btn-outline-primary">Register</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <footer>
      <p>&copy; 2024 Household Services. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
body {
  background-color: #002b36; /* Base background color (Solarized Dark) */
  color: #839496; /* Base text color */
  margin: 0;
}

.home-header {
  background-color: #073642; /* Solarized Dark background for header */
  border-bottom: 5px solid #00fec3; /* Accent color */
}

.home-header h1 {
  color: #fdf6e3; /* Light color for header text */
}

.home-header p {
  color: #93a1a1; /* Light color for paragraph */
}

.btn-outline-primary {
  color: #00fec3; /* Button text color */
  border-color: #00fec3; /* Button border color */
}

.btn-outline-primary:hover {
  background-color: #00fec3; /* Button hover color */
  color: #073642; /* Text color on hover */
  border-color: #00fec3;
}

.container {
  margin-top: 20px;
}

i {
  border: 1px solid #00fec3;
  border-radius: 50%;
  height: 100px;
  width: 100px;
  margin-left: auto;
  margin-right: auto;
  padding: 20px;
}

footer {
  display: flex;
  background-color: #073642;
  min-height: 80px;
  justify-content: center;
  align-items: center;
  border-top: 5px solid #00fec3;
}

/* Additional styles for card */
.card {
  margin-top: 10%;
  border: 2px solid #00fec3;
  height: 450px; /* Ensuring all cards have the same height */
}

.bg-base02 {
  background-color: #073642; /* Solarized base02 color for card background */
}

/* Hover effect for cards */
.card-hover {
  transition: all 0.5s ease; /* Smooth transition for hover effect */
}

.card-hover:hover {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3); /* Add shadow on hover */
  transform: translateY(-2px) scale(1.01); /* Lift effect on hover */
}
</style>
