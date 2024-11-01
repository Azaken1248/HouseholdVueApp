<template>
  <div class="d-flex flex-column min-vh-100">
    <header class="home-header text-center text-white py-5">
      <h2>Welcome to Household Services</h2>
      <p>Your one-stop solution for all household needs</p>
    </header>

    <div class="container mt-4 flex-grow-1">
    <router-view />

      <!-- Only show the service cards if the user is not logged in and is not on Login or Registration pages -->
      <div v-if="!isLoggedIn && !isOnLoginOrRegister" class="row">
        <div class="col-md-4" v-for="(roleCard, index) in roleCards" :key="index">
          <div class="card text-center text-white bg-base02 mb-4 card-hover">
            <div class="card-body d-flex flex-column justify-content-between" style="height: 300px;">
              <h5 class="card-title">{{ roleCard.title }}</h5>
              <i :class="roleCard.icon + ' fa-3x mb-3'"></i>
              <p class="card-text">{{ roleCard.text }}</p>
              <div>
                <router-link :to="{ name: 'Login', params: { role: roleCard.role } }" class="btn btn-outline-primary me-2">Login</router-link>
                <router-link :to="{ name: 'Registration', params: { role: roleCard.role } }" class="btn btn-outline-primary">Register</router-link>
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
import { ref, computed } from 'vue';
import { useRoute } from 'vue-router';

export default {
  name: "App",
  setup() {
    const isLoggedIn = ref(!!localStorage.getItem('access_token')); // Check if the user is logged in based on localStorage
    const route = useRoute();
    const roleCards = [
      {
        title: 'User',
        icon: 'fas fa-user-tie',
        text: 'Login or Register as a user to access household services.',
        role: 'User'
      },
      {
        title: 'Admin',
        icon: 'fas fa-user-shield',
        text: 'Manage users and services efficiently.',
        role: 'Admin'
      },
      {
        title: 'Service Professional',
        icon: 'fas fa-user-cog',
        text: 'Join as a professional to offer your services.',
        role: 'Service Professional'
      },
    ];

    const isOnLoginOrRegister = computed(() => {
      return route.path.includes('/login') || route.path.includes('/register') || route.path.includes('/dashboard');
    });

    console.log(!ref(isOnLoginOrRegister))
    return {
      isLoggedIn,
      roleCards,
      isOnLoginOrRegister,
    };
  },
};
</script>

<style>
body {
  background-color: #002b36; /* Base background color (Solarized Dark) */
  color: #839496; /* Base text color */
  margin: 0;
  height: fit-content;
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
