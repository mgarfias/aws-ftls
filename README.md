How I built a fault tolerant, load balancing network at AWS on the cheap
========================================================================

Architecture
------------

I leveraged ELB and multiple regions, to make sure a regional outage would not disrupt the site.  Two ELBs, one in each region.


How I set it all up
-------------------

1. Wrote a boto script to initialize an S3 bucket where the puppet configs live, and copy them up.
2. Wrote a cloud-init script to install puppet, then install the puppet packages, and finally kick off the first puppet run against the freshly installed config.
3. Wrote boto script to query AWS and grab the isntance IDs from them, and create the ELBs/EIPs.
4. 