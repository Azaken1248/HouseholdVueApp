<template>
  <div class="container mt-5">
    <h2>Search Services</h2>
    <form>
      <div class="mb-3">
        <label for="search" class="form-label">Search by Name, Location, or Pin Code</label>
        <input type="text" class="form-control" id="search" placeholder="Enter search criteria" />
      </div>
      <button type="submit" class="btn btn-primary">Search</button>
    </form>
    <div class="mt-4">
      <h3>Results</h3>
      <ul class="list-group">
        <li class="list-group-item" v-for="service in services" :key="service.id">
          {{ service.name }} - {{ service.location }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "ServiceSearch",
  data() {
    return {
      services: [
        { id: 1, name: "Plumbing", location: "New York" },
        { id: 2, name: "Electrical Repair", location: "Los Angeles" },
      ],
    };
  },
};
</script>
