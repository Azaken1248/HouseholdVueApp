<template>
  <div class="container mt-5" v-if="isAuthenticated">
    <h2>Admin Dashboard</h2>
    <div class="row">
      <!-- Manage Users Section -->
      <div class="col-md-6">
        <h3>Manage Users</h3>
        <table class="table">
          <thead>
            <tr>
              <th>Username</th>
              <th>Email</th>
              <th>Role</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="user in users" :key="user.id">
              <td>{{ user.username }}</td>
              <td>{{ user.email }}</td>
              <td>{{ user.role }}</td>
              <td>{{ user.status }}</td>
              <td>
                <button class="btn btn-warning btn-sm" @click="updateUserStatus(user.id, 'blocked')">Block</button>
                <button class="btn btn-success btn-sm" @click="updateUserStatus(user.id, 'approved')">Approve</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Service Requests Section -->
      <div class="col-md-6">
        <h3>Service Requests</h3>
        <table class="table">
          <thead>
            <tr>
              <th>Request ID</th>
              <th>User ID</th>
              <th>Service ID</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="serviceRequests.length === 0">
              <td colspan="5">No service requests available</td>
            </tr>
            <tr v-else v-for="request in serviceRequests" :key="request.id">
              <td>{{ request.id }}</td>
              <td>{{ request.user_id }}</td>
              <td>{{ request.service_id }}</td>
              <td>{{ request.status }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <button class="btn btn-success btn-sm" @click="logoutUser">Logout</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: "AdminDashboard",
  setup() {
    const users = ref([]);
    const serviceRequests = ref([]);
    const isAuthenticated = ref(false);
    const router = useRouter();

    const fetchUsers = async () => {
      try {
        const token = localStorage.getItem('access_token');
        const userResponse = await axios.get('http://localhost:5000/api/users', {
          headers: { Authorization: `Bearer ${token}` }
        });
        users.value = userResponse.data;
      } catch (error) {
        console.error("Error fetching users:", error);
        router.push({ name: 'Login' });
      }
    };

    const fetchServiceRequests = async () => {
      try {
        const token = localStorage.getItem('access_token');
        const requestResponse = await axios.get('http://localhost:5000/api/service-requests', {
          headers: { Authorization: `Bearer ${token}` }
        });
        serviceRequests.value = requestResponse.data;
      } catch (error) {
        console.error("Error fetching service requests:", error);
      }
    };

    const updateUserStatus = async (userId, status) => {
      try {
        const token = localStorage.getItem('access_token');
        await axios.patch(`http://localhost:5000/api/users/${userId}`, {
          status: status
        }, {
          headers: { Authorization: `Bearer ${token}` }
        });
        // Update the user's status locally
        const user = users.value.find(u => u.id === userId);
        if (user) {
          user.status = status;
        }
      } catch (error) {
        console.error(`Error updating user status to ${status}:`, error);
      }
    };

    const logoutUser = () => {
      localStorage.removeItem("access_token");
      isAuthenticated.value = false; // Update the authentication state
      router.push({ name: 'Login' }); // Redirect to the home page or login page
    };

    const updateRequestStatus = async (requestId, status) => {
      try {
        const token = localStorage.getItem('access_token');
        await axios.patch(`http://localhost:5000/api/service-requests/${requestId}`, {
          status: status
        }, {
          headers: { Authorization: `Bearer ${token}` }
        });
        // Update local data
        const request = serviceRequests.value.find(r => r.id === requestId);
        if (request) {
          request.status = status;
        }
      } catch (error) {
        console.error(`Error updating request status to ${status}:`, error);
      }
    };

    onMounted(() => {
      const token = localStorage.getItem('access_token');
      if (token) {
        fetchUsers();
        fetchServiceRequests();
        isAuthenticated.value = true; // Set authenticated state to true if token is present
      } else {
        router.push({ name: 'Login' }); // Redirect if not authenticated
      }
    });

    return { users, serviceRequests, isAuthenticated, updateUserStatus, updateRequestStatus, logoutUser };
  }
};
</script>

<style scoped>
  table th {
    background-color: #073642;
    border: 1px solid #00fec3;
    color: #00fec3;
  }
  table tr td {
    background-color: #073642;
    border: 1px solid #00fec3;
    color: #00fec3;
  }
  button {
    margin: 10px;
    background-color: #073642;
    color: #00fec3;
    border-color: #00fec3;
  }
  button:hover{
    background-color: #00fec3; 
    color: #073642; 
  }
</style>
