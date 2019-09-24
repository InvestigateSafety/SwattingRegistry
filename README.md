# SwattingRegistry

* Inspired by the work of Sean Whitcomb, https://www.linkedin.com/in/seanpwhitcomb, who designed the first ever publicly promoted Swatting Concerns Registry, see https://www.seattle.gov/police/need-help/swatting, https://www.wired.com/story/how-to-stop-swatting-before-it-happens-seattle/

## Project manager: Tim Clemans

SwattingRegistry is a demonstration project by InvestigateSafety's demonstration technolgy development group. It's purpose is to save lives by alerting law enforcement that a citizen's report to the agency is likely false, confirming that target(s) is not at target location or via internet video stream that no crime is in progress, automating investigation procedures, and providing feedback on policies and complaiance to them

Long term implementation goal: transfer ownership of site to FBI or DHS domain would be swattingregistry.gov with a contract with Code for America (software development), Axon (intergration), Mark43 (intergration), Rave, 

## Independent Reviewers

* Sean Whitcomb: Seattle Police Department Sergeant in charge of the Public Affairs Unit https://www.linkedin.com/in/seanpwhitcomb
* Chris Metcalf: Formerly Developer Relations for Socrata
* Elisa Huntley: 
  * 10 years as a police analyst (20,800 hours approximately)
  * trained in SQL and have delved into the back end of the Records Management System (Versaterm)
  * Worked with the SPD analysts directly 
  * https://www.linkedin.com/in/elisahuntley/
* Kevin Fray: Mark43 Pre-Sales Lead Principal Solutions Architect https://www.linkedin.com/in/kevinfray/

## Hybird Open and Closed Source Strategy

Intergrations are in closed source repos one repo per intergration and owned jointly by the vendor and ulimiately Code for America (if CA agrees to take over development).

## Anti State Public Records Act and Federal Freedom of Information Act Request Disclosure Strategy

Data would be owned by FBI or DHS or both with registry data only shared during swatting.

## Components

Combination of:

* Opt-in registry: household model written, non household like gamer's business location is needed
  * Auto submission to Rave Facility, CAD/RMS systems via intergration either screen scraper or API
* Swatting detection system or demertaion based on history that report is real https://www.defcon.org/images/defcon-22/dc-22-presentations/Quaddi-R3plicant-Hefley/DEFCON-22-Quaddi-R3plicant-Hefley-Hacking-911-UPDATED.pdf https://www.youtube.com/watch?v=mBOLml3yLBY
  * 911 caller history
  * Address history
  * History of indivuals associated with address
  * Billing data & emergency regisration
  * VOIP provider (consumer [Vonage, Xfinity] vs developer [Twillio, FlowRoute])
* Threat analysis
  * Web crawler
* Realtime cross agency sharing
  * False reporting by terrorist group
* Criminal investigation assistance 
  * Evidence archiving
    * Message boards
    * Video streams
    * Chats
  * Auto warrant request writing
* Address to phone numbers auto lookup 
* Auto phone call and messaging
* Policies registry and incident investigation by InvestigateSafety
  * Structured database of false reporting by citizen that ended up routed to dispatch
  
## Vulnerability Relays 

### Noonlight

* GPS spoofing
